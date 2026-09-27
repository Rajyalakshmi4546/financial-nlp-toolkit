<!-- markdownlint-disable -->

# API Overview

## Modules

- [`financial-nlp-toolkit.api`](./financial-nlp-toolkit.api.md#module-opyratorapi)
- [`financial-nlp-toolkit.api.fastapi_app`](./financial-nlp-toolkit.api.fastapi_app.md#module-opyratorapifastapi_app)
- [`financial-nlp-toolkit.api.fastapi_utils`](./financial-nlp-toolkit.api.fastapi_utils.md#module-opyratorapifastapi_utils): Collection of utilities for FastAPI apps.
- [`financial-nlp-toolkit.components`](./financial-nlp-toolkit.components.md#module-opyratorcomponents)
- [`financial-nlp-toolkit.components.outputs`](./financial-nlp-toolkit.components.outputs.md#module-opyratorcomponentsoutputs)
- [`financial-nlp-toolkit.components.types`](./financial-nlp-toolkit.components.types.md#module-opyratorcomponentstypes)
- [`financial-nlp-toolkit.core`](./financial-nlp-toolkit.core.md#module-opyratorcore)
- [`financial-nlp-toolkit.export`](./financial-nlp-toolkit.export.md#module-opyratorexport)
- [`financial-nlp-toolkit.tasks`](./financial-nlp-toolkit.tasks.md#module-opyratortasks)
- [`financial-nlp-toolkit.ui`](./financial-nlp-toolkit.ui.md#module-opyratorui)
- [`financial-nlp-toolkit.ui.schema_utils`](./financial-nlp-toolkit.ui.schema_utils.md#module-opyratoruischema_utils)
- [`financial-nlp-toolkit.ui.streamlit_ui`](./financial-nlp-toolkit.ui.streamlit_ui.md#module-opyratoruistreamlit_ui)
- [`financial-nlp-toolkit.ui.streamlit_utils`](./financial-nlp-toolkit.ui.streamlit_utils.md#module-opyratoruistreamlit_utils): Hack to add per-session state to Streamlit.
- [`financial-nlp-toolkit.utils`](./financial-nlp-toolkit.utils.md#module-opyratorutils)

## Classes

- [`outputs.ClassificationOutput`](./financial-nlp-toolkit.components.outputs.md#class-classificationoutput)
- [`outputs.ScoredLabel`](./financial-nlp-toolkit.components.outputs.md#class-scoredlabel)
- [`types.FileContent`](./financial-nlp-toolkit.components.types.md#class-filecontent)
- [`core.Financial NLP Toolkit`](./financial-nlp-toolkit.core.md#class-financial-nlp-toolkit)
- [`export.ExportFormat`](./financial-nlp-toolkit.export.md#class-exportformat): An enumeration.
- [`streamlit_ui.InputUI`](./financial-nlp-toolkit.ui.streamlit_ui.md#class-inputui)
- [`streamlit_ui.OutputUI`](./financial-nlp-toolkit.ui.streamlit_ui.md#class-outputui)
- [`streamlit_utils.SessionState`](./financial-nlp-toolkit.ui.streamlit_utils.md#class-sessionstate)

## Functions

- [`fastapi_app.create_api`](./financial-nlp-toolkit.api.fastapi_app.md#function-create_api)
- [`fastapi_app.launch_api`](./financial-nlp-toolkit.api.fastapi_app.md#function-launch_api)
- [`fastapi_utils.as_form`](./financial-nlp-toolkit.api.fastapi_utils.md#function-as_form): Adds an as_form class method to decorated models.
- [`fastapi_utils.patch_fastapi`](./financial-nlp-toolkit.api.fastapi_utils.md#function-patch_fastapi): Patch function to allow relative url resolution.
- [`core.get_callable`](./financial-nlp-toolkit.core.md#function-get_callable): Import a callable from an string.
- [`core.get_input_type`](./financial-nlp-toolkit.core.md#function-get_input_type): Returns the input type of a given function (callable).
- [`core.get_output_type`](./financial-nlp-toolkit.core.md#function-get_output_type): Returns the output type of a given function (callable).
- [`core.is_compatible_type`](./financial-nlp-toolkit.core.md#function-is_compatible_type): Returns `True` if the type is financial-nlp-toolkit-compatible.
- [`core.name_to_title`](./financial-nlp-toolkit.core.md#function-name_to_title): Converts a camelCase or snake_case name to title case.
- [`schema_utils.get_single_reference_item`](./financial-nlp-toolkit.ui.schema_utils.md#function-get_single_reference_item)
- [`schema_utils.is_multi_enum_property`](./financial-nlp-toolkit.ui.schema_utils.md#function-is_multi_enum_property)
- [`schema_utils.is_multi_file_property`](./financial-nlp-toolkit.ui.schema_utils.md#function-is_multi_file_property)
- [`schema_utils.is_object_list_property`](./financial-nlp-toolkit.ui.schema_utils.md#function-is_object_list_property)
- [`schema_utils.is_property_list`](./financial-nlp-toolkit.ui.schema_utils.md#function-is_property_list)
- [`schema_utils.is_single_boolean_property`](./financial-nlp-toolkit.ui.schema_utils.md#function-is_single_boolean_property)
- [`schema_utils.is_single_datetime_property`](./financial-nlp-toolkit.ui.schema_utils.md#function-is_single_datetime_property)
- [`schema_utils.is_single_dict_property`](./financial-nlp-toolkit.ui.schema_utils.md#function-is_single_dict_property)
- [`schema_utils.is_single_enum_property`](./financial-nlp-toolkit.ui.schema_utils.md#function-is_single_enum_property)
- [`schema_utils.is_single_file_property`](./financial-nlp-toolkit.ui.schema_utils.md#function-is_single_file_property)
- [`schema_utils.is_single_number_property`](./financial-nlp-toolkit.ui.schema_utils.md#function-is_single_number_property)
- [`schema_utils.is_single_object`](./financial-nlp-toolkit.ui.schema_utils.md#function-is_single_object)
- [`schema_utils.is_single_reference`](./financial-nlp-toolkit.ui.schema_utils.md#function-is_single_reference)
- [`schema_utils.is_single_string_property`](./financial-nlp-toolkit.ui.schema_utils.md#function-is_single_string_property)
- [`schema_utils.resolve_reference`](./financial-nlp-toolkit.ui.schema_utils.md#function-resolve_reference)
- [`streamlit_ui.function_has_named_arg`](./financial-nlp-toolkit.ui.streamlit_ui.md#function-function_has_named_arg)
- [`streamlit_ui.has_input_ui_renderer`](./financial-nlp-toolkit.ui.streamlit_ui.md#function-has_input_ui_renderer)
- [`streamlit_ui.has_output_ui_renderer`](./financial-nlp-toolkit.ui.streamlit_ui.md#function-has_output_ui_renderer)
- [`streamlit_ui.is_compatible_audio`](./financial-nlp-toolkit.ui.streamlit_ui.md#function-is_compatible_audio)
- [`streamlit_ui.is_compatible_image`](./financial-nlp-toolkit.ui.streamlit_ui.md#function-is_compatible_image)
- [`streamlit_ui.is_compatible_video`](./financial-nlp-toolkit.ui.streamlit_ui.md#function-is_compatible_video)
- [`streamlit_ui.launch_ui`](./financial-nlp-toolkit.ui.streamlit_ui.md#function-launch_ui)
- [`streamlit_ui.render_streamlit_ui`](./financial-nlp-toolkit.ui.streamlit_ui.md#function-render_streamlit_ui)
- [`streamlit_utils.get_current_session`](./financial-nlp-toolkit.ui.streamlit_utils.md#function-get_current_session)
- [`streamlit_utils.get_session_state`](./financial-nlp-toolkit.ui.streamlit_utils.md#function-get_session_state): Gets a SessionState object for the current session.


---

_This file was automatically generated via [lazydocs](https://github.com/Rajyalakshmi Nelakurthi/lazydocs)._
