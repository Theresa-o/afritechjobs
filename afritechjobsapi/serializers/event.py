from rest_framework import serializers
from afritechjobsapi.models import (Event)


class EventSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Event
        # put back banner image field after updating the model and deleting previous content from admin
        fields = [
            'id',
            'event_name',
            'event_details',
            'author',
            'event_host',
            'event_date',
            'registration_fees',
            'date_created',
            'date_updated',
            'is_attending',
        ]