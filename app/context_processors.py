from .models import PlantCareLog, Plant, User


def plant_monitoring_context(request):
    """
    Adds global context variables that will be available in every template.
    """
    context = {}

    # Example: Check if the user is authenticated
    if request.user.is_authenticated:
        # Get the user's plants (or care logs, if applicable)
        user_plants = Plant.objects.filter(user=request.user)

        # Example: Number of plants needing care
        plants_needing_care = PlantCareLog.objects.filter(
            plant__in=user_plants,
            status='NEEDS_ATTENTION'
        ).count()

        # Add to the context dictionary
        context['plants_needing_care'] = plants_needing_care
        context['user_profile'] = request.user.profile if hasattr(request.user, 'profile') else None

    return context
