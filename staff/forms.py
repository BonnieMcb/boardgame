from django import forms
from games.models import Product
from events.models import Events


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category_id', 'mechanic_id', 'names',
                  'min_players', 'max_players', 'avg_time',
                  'min_time', 'max_time', 'age', 'price',
                  'image_url', 'rank', 'bgg_url', 'game_id',
                  'year', 'avg_rating', 'geek_rating',
                  'num_votes', 'owned', 'designer', 'weight',
                  'is_visible', 'is_membership')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('name', 'datetime', 'description', 'image',
                  'offsite_url', 'member_only', 'signed_up_users')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
