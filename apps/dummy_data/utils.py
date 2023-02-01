from django.db import transaction


def formset_validation(request, form, formset):
    with transaction.atomic():
        form = form.save(commit=False)
        form.user = request.user
        form.save()
        for column in formset:
            if column in formset.deleted_forms:
                continue
            data = column.save(commit=False)
            data.schema = form
            data.save()
