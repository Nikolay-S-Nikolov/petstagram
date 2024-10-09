from django import template

register = template.Library()


def create_button(context, check_funk, result_function, arrow_class_name):
    pet_name_pattern = context["pet_name_pattern"]

    search_query = ""
    if pet_name_pattern:
        search_query = f"&pet_search_pattern={pet_name_pattern}"

    page_query = "#"
    class_name = "disabled"
    if check_funk():
        page_query = f"?page={result_function()}"
        class_name = ""

    return {
        "page_query": page_query,
        "search_query": search_query,
        "class_name": class_name,
        "arrow_class": f"fa-solid {arrow_class_name}"
    }


@register.inclusion_tag("common/tags/prev_button.html", takes_context=True)
def prev_button(context):
    page_obj = context["page_obj"]

    return create_button(context, page_obj.has_previous, page_obj.previous_page_number, "fa-arrow-left")



@register.inclusion_tag("common/tags/prev_button.html", takes_context=True)
def next_button(context):
    page_obj = context["page_obj"]

    return create_button(context, page_obj.has_next, page_obj.next_page_number, "fa-arrow-right")
