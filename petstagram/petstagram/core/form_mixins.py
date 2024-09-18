class ReadOnlyFieldsMixin:
    read_only_fields = ()

    def _apply_read_only_fields(self):
        for field_name in self.readonly_fields_name:
            self.fields[field_name].widget.attrs["readonly"] = "readonly"

    @property
    def readonly_fields_name(self):
        if self.read_only_fields == "__all__":
            return self.fields.keys()
        return self.read_only_fields