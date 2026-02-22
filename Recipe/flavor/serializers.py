from rest_framework import serializers
from .models import Recipe, MealPlan, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe.ingredients.through
        fields = ['ingredient']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.PrimaryKeyRelatedField(many = True, queryset=Ingredient.objects.all())
    
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'instructions', 'ingredients', 'created_at']
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return value

class MealPlanSerializer(serializers.ModelSerializer):
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all())
    
    class Meta:
        model = MealPlan
        fields = ['id', 'recipe', 'date', 'meal_type']
