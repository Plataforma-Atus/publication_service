from uuid import uuid4

from django.db import models


class UF(models.Model):
    uf = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.uf


class City(models.Model):
    uf = models.ForeignKey(UF, on_delete=models.PROTECT)
    name = models.CharField(max_length=250)
    size = models.CharField(max_length=50, null=False, blank=False)
    capital = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    name = models.CharField(max_length=50)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    official_newspaper = models.BooleanField(default=False)
    active_newspaper = models.BooleanField(default=True)
    printed = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True, editable=False)
    modify_at = models.DateTimeField(auto_now=True, editable=False)
    deadline_days = models.DateField(null=True)
    deadline_hour = models.IntegerField(null=True)

    def __str__(self):
        return str(self.name)


class Font(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)
    id = models.IntegerField(primary_key=True, null=False, blank=False)

    def __str__(self):
        return self.name


class NewspaperSection(models.Model):
    name_section = models.CharField(max_length=50)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    newspaper_id = models.ForeignKey(Newspaper, on_delete=models.CASCADE)
    width_1 = models.DecimalField(max_digits=4, decimal_places=2, default=8, null=False, blank=False)
    width_2 = models.DecimalField(max_digits=4, decimal_places=2, default=17, null=False, blank=False)
    width_3 = models.DecimalField(max_digits=4, decimal_places=2, default=25, null=False, blank=False)
    width_4 = models.DecimalField(max_digits=4, decimal_places=2, default=0, null=False, blank=True)
    width_5 = models.DecimalField(max_digits=4, decimal_places=2, default=0, null=False, blank=True)
    width_6 = models.DecimalField(max_digits=4, decimal_places=2, default=0, null=False, blank=True)
    width_7 = models.DecimalField(max_digits=4, decimal_places=2, default=0, null=False, blank=True)
    width_8 = models.DecimalField(max_digits=4, decimal_places=2, default=0, null=False, blank=True)
    width_9 = models.DecimalField(max_digits=4, decimal_places=2, default=0, null=False, blank=True)
    width_10 = models.DecimalField(max_digits=4, decimal_places=2, default=0, null=False, blank=True)
    gutter = models.DecimalField(max_digits=4, decimal_places=3, default=0.206)
    height = models.DecimalField(max_digits=3, decimal_places=1)
    minimum_height = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    maximum_height_budget = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    font_name = models.ForeignKey(Font, on_delete=models.SET_DEFAULT, related_name="name_primary",
                                  default="Times New Roman")
    font_name_alternative = models.ForeignKey(Font, on_delete=models.SET_DEFAULT, related_name="name_secondary",
                                              default="Arial")
    font_size = models.DecimalField(max_digits=4, decimal_places=2, default=7)
    font_leading = models.DecimalField(max_digits=4, decimal_places=2, default=8)
    font_size_company = models.DecimalField(max_digits=4, decimal_places=2, default=12)
    font_leading_company = models.DecimalField(max_digits=4, decimal_places=2, default=13)
    tracking_choices = (
        ('0', 'Normal'),
        ('-10', 'Low'),
        ('-20', 'Medium'),
        ('-30', 'High'),
        ('-40', 'Warning: Ultra'),
    )
    tracking = models.CharField(max_length=50, choices=tracking_choices, default='Normal')
    condensation = models.DecimalField(max_digits=5, decimal_places=2, default=100)
    format_choices = (
        ('.pdf', 'Pdf'),
        ('.docx', 'Docx'),
        ('.rtf', 'Rtf'),
        ('.doc', 'Doc 97/03'),
        ('.odt', 'Odt'),
    )
    format_out = models.CharField(max_length=5, choices=format_choices, default='PDF')
    price_cm = models.DecimalField(max_digits=7, decimal_places=2, default=150, verbose_name="price_cm_column")
    price_cm_square = models.DecimalField(max_digits=7, decimal_places=2, default=150, null=True)
    price_extra_color = models.DecimalField(max_digits=7, decimal_places=2, default=150, null=True, blank=True)
    bold = models.BooleanField(default=True, null=True)
    italic = models.BooleanField(default=True, null=True)
    underline = models.BooleanField(default=True, null=True)
    edge = models.BooleanField(default=False)
    height_round = models.BooleanField(default=True, null=True)
    deadline_days = models.DateField(null=True, blank=True)
    deadline_hour = models.IntegerField(null=True, blank=True)
    circulate_days = models.DateField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_section


class PublicationTypeName(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=True)
    quantity_days = models.IntegerField(null=True)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PublicationType(models.Model):
    name = models.ForeignKey(PublicationTypeName, on_delete=models.SET_NULL, null=True, blank=False)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    newspaper_section_id = models.ForeignKey(NewspaperSection, on_delete=models.SET_NULL, null=True, blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)
    instructions = models.TextField(max_length=1000, null=True, blank=True)
    margin = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    estimated_budget_delivery = models.PositiveIntegerField(default=2)
    font_name = models.ForeignKey(Font, on_delete=models.SET_DEFAULT, related_name="name_special",
                                  default="Times New Roman")
    font_size = models.DecimalField(max_digits=4, decimal_places=2, default=6, null=True, blank=True)
    font_leading = models.DecimalField(max_digits=4, decimal_places=2, default=6, null=True, blank=True)
    font_size_company = models.DecimalField(max_digits=4, decimal_places=2, default=6, null=True, blank=True)
    font_leading_company = models.DecimalField(max_digits=4, decimal_places=2, default=6, null=True, blank=True)
    bold = models.BooleanField(default=True, null=True)
    italic = models.BooleanField(default=True, null=True)
    underline = models.BooleanField(default=True, null=True)
    tracking_choices = (
        ('0', 'Normal'),
        ('-10', 'Low'),
        ('-20', 'Medium'),
        ('-30', 'High'),
        ('-40', 'Warning: Ultra'),
    )
    tracking = models.CharField(max_length=50, choices=tracking_choices, default='Normal')
    condensation = models.DecimalField(max_digits=5, decimal_places=2, default=100)
    format_choices = (
        ('0', 'Company name + Employer number + title + Flowing text'),
        ('1', 'Title or Employer number or Identity + Flowing text'),
        ('2', 'Flowing text'),
        ('3', 'Tagged'),
        ('4', 'Balance'),
    )
    special_format = models.BooleanField(default=True)
    format = models.CharField(max_length=50, choices=format_choices, default='0')

    def __str__(self):
        return str(self.name.name)


class Client(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=200, null=False, unique=True)
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    phone = models.CharField(max_length=12, null=True, blank=True)
    phone_secondary = models.CharField(max_length=12, null=True, blank=True)
    cellphone = models.CharField(max_length=13, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length=150)
    document_name = models.URLField(max_length=150, null=False, blank=False)
    day_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )
    days = models.CharField(max_length=4, choices=day_choices, default='1')
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    publication_type_id = models.ForeignKey(PublicationType, on_delete=models.PROTECT, null=False, blank=False)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)
    calculated_price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
    calculated_price_unity = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
    height = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
