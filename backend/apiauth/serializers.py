from rest_framework import serializers, status
from apiauth.models import UserProfile, User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = UserProfile
        fields = ['user', 'gender', 'roll_number', 'phone', 'prog', 'year', 'branch']
    #gender = serializers.CharField(max_length=1)
    #roll_number = serializers.CharField(max_length=15)
    #phone = serializers.CharField(max_length=10)
    #prog = serializers.CharField(max_length=5)
    #year = serializers.CharField(max_length=1)
    #avatar = serializers.ImageField(default='default_member.png')
    #branch = serializers.CharField(max_length=5)
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        student = UserProfile.objects.update_or_create(user=user, gender=validated_data.pop('gender'),roll_number=validated_data.pop('roll_number'),
                                            phone=validated_data.pop('phone'), prog=validated_data.pop('prog'), year=validated_data.pop('year'),
                                            branch=validated_data.pop('branch'))                                          
        return student
    def update(self, validated_data, instance):
        instance.user = validated_data.get("user", instance.user)
        instance.gender = validated_data.get("gender", instance.gender)
        instance.roll_number = validated_data.get("roll_number", instance.roll_number)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.prog = validated_data.get("prog", instance.prog)
        instance.year = validated_data.get("year", instance.year)
        instance.branch = validated_data.get("branch", instance.branch)
        instance.save()
        return instance