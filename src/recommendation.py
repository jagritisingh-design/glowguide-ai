def recommend_products(skin_type):
    recommendations = {
        "Dry": ["Moisturizer", "Hydrating Cleanser"],
        "Oily": ["Gel Cleanser", "Oil-Free Moisturizer"],
        "Combination": ["Gentle Cleanser", "Light Moisturizer"],
        "Sensitive": ["Fragrance-Free Moisturizer"]
    }

    return recommendations.get(skin_type, [])