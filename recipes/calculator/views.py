from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'salad': {
        'Оливки зеленые, банка': 0.5,
        'Листья салата, пучок': 1,
        'Шампиньоны (свежие), шт': 8,
        'Сыр Фета, г': 100,
        'Масло оливковое, ст.л.': 2
    }
}


def calc(request, recipe):
    context = dict()
    dish = DATA.get(recipe)
    servings = int(request.GET.get('servings', '1'))
    if dish:
        for k,v in dish.items():
            context[k] = v * servings
    return render(request, 'calculator/index.html', {'recipe': context})
