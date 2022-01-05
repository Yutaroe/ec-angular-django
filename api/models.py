import uuid
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser,BaseUserManager
# from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
# from django.contrib.auth.base_user import BaseUserManager
from django.db.models.deletion import CASCADE


def upload_coffee_path(instance, filename):
    ext = filename.split('.')[-1]
    return '/'.join(['posts', str(instance.coffee_name)+str(".")+str(ext)])

# Create your models here.

class UserManager(BaseUserManager):
    """ユーザーマネージャー."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a user with the given username, email, and
        password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル."""
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('ニックネーム'), max_length=150, blank=True, null=True)

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s' % (self.username)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.username

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Coffee(models.Model):
    coffee_name = models.CharField('商品名', max_length=100, blank=False)
    coffee_detail = models.CharField('商品詳細', max_length=200, blank=False)
    img = models.ImageField(blank=True, null=True, upload_to=upload_coffee_path)
    coffee_priceL = models.IntegerField('商品Lサイズ料金', blank=False, null=False)
    coffee_priceM = models.IntegerField('商品Mサイズ料金', blank=False, null=False)

    def __str__(self):
        return self.coffee_name


class Topping(models.Model):
    topping_name = models.CharField('トッピング名', max_length=100, blank=False)    
    topping_priceL = models.IntegerField('トッピングLサイズ料金', blank=False, null=False)
    topping_priceM = models.IntegerField('トッピングMサイズ料金', blank=False, null=False)

    def __str__(self):
        return self.topping_name

class Carts(models.Model):
    order_name = models.CharField('注文者名', max_length=30, blank=True, null=True)
    addressnumber = models.CharField('郵便番号', max_length=9, blank=True, null=True)
    address = models.CharField('住所', max_length=100, blank=True, null=True)
    email = models.EmailField('メールアドレス', max_length=100, blank=True, null=True)
    order_date = models.DateField('配達日', blank=True, null=True)
    order_time = models.CharField('配達時間',max_length=20, blank=True, null=True)
    tel = models.CharField('電話番号', max_length=14, blank=True, null=True)
    status = models.IntegerField('注文状況', blank=True, null=True)
    userCart = models.ForeignKey(User, on_delete=CASCADE, related_name='userCart')



class OrderCoffee(models.Model):
    item_number = models.IntegerField('数量', blank=False, null=False)
    coffee_id = models.ForeignKey(Coffee, on_delete=CASCADE)
    item_size = models.CharField('商品サイズ', max_length=6, blank=False, null=False)
    toppings = models.ManyToManyField(Topping, blank=True)
    carts = models.ForeignKey(Carts, on_delete=CASCADE, related_name='carts')

    