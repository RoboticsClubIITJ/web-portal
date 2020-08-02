from django.contrib.auth import authenticate
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    error_messages = {
        'invalid_login': _(
            "Please enter a correct email and password. Note that both fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive.")
    }

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
        self.user_cache = None

    def validate(self, attrs):
        username = attrs.get('email')
        password = attrs.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise serializers.ValidationError(
                    detail=_("Please enter a correct email and password. Note that both fields may be case-sensitive."),
                    code="invalid_login"
                )
            elif not self.user_cache.is_active:
                raise serializers.ValidationError(
                    detail=_("This account is inactive."),
                    code='inactive',
                )
        return attrs

    def get_user(self):
        return self.user_cache

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
