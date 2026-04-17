from utils.crowd import get_crowd_density

def build_context():
    crowd_data = get_crowd_density()

    context_parts = []

    for zone, value in crowd_data.items():
        if value > 70:
            status = "high"
        elif value > 40:
            status = "moderate"
        else:
            status = "low"

        context_parts.append(f"{zone} crowd is {status}")

    return ", ".join(context_parts)
