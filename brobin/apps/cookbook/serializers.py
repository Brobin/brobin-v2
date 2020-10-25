from rest_framework import serializers

from .models import Recipe, Ingredient, IngredientAmount, Step


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['text']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['name']


class IngredientAmountSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()

    class Meta:
        model = IngredientAmount
        fields = ['ingredient', 'amount']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientAmountSerializer(many=True)
    steps = StepSerializer(many=True)

    class Meta:
        model = Recipe
        fields = [
            'title', 'created', 'updated', 'slug',
            'notes', 'prep_time', 'cook_time',
            'ingredients', 'steps'
        ]
