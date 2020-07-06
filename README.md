1 - Installation of 3 components
```
generate -g python -i specs/payment-api.yaml -o ./ --library asyncio --additional-properties="packageName=payment,generateSourceCodeOnly=true" --skip-validate-spec

openapi-generator generate -g python -i specs/activity-api.yaml -o ./ --library asyncio --additional-properties="packageName=activity,generateSourceCodeOnly=true" --skip-validate-spec

openapi-generator generate -g python -i specs/market-api.yaml -o ./ --library asyncio --additional-properties="packageName=market,generateSourceCodeOnly=true" --skip-validate-spec
```
2 - Remove api_client, configuration, rest, exceptions.py files from components, 
```
Rename;
<component_name>.api_client     -> src.api_client
<component_name>.configuration  -> src.configuration
<component_name>.rest           -> src.rest
<component_name>.exceptions     -> src.exceptions
```

3 - Remove Api_Client imports from \_\_init\_\_ on all components

4 - Edits (one time)
```
configuration.py#19     -> from typing import Callable, Optional
configuration.py#L112   -> self.access_token = None
configuration.py#L123   -> self.refresh_api_key_hook = Optional[Callable]
api_client.py#58 	-> int if six.PY3 else long -> int
```
