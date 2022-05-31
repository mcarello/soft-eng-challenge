from drf_yasg import openapi

mothership_create_response_schema = {
    "201": openapi.Response(
        description="Mothership created",
        examples={
            "application/json": {
            "id": 2,
            "name": "ZXS978",
            "capacity": 9
            }
        }
    ),
    "400": openapi.Response(
        description="Bad request",
        examples={
            "application/json": {
        "error": "name parameter does not exist"
        }
        }
    ),
}

mothership_detail_response_schema = {
    "201": openapi.Response(
        description="Create a Mothership",
        examples={
            "application/json": {
            "id": 4,
            "name": "ZXS978",
            "capacity": 9
        }
        }
    ),    
    "400": openapi.Response(
        description="Bad request",
        examples={
            "application/json": {
        "error": "Mothership 1242 does not Exist"
        }
        }
    ),    
}

mothership_delete_response_schema = {
    "201": openapi.Response(
        description="Delete a Mothership",
        examples={
            "application/json": {
            "msg": "Mothership 2 deleted"
        }
        }
    ),    
    "400": openapi.Response(
        description="Bad request",
        examples={
            "application/json": {
        "error": "Mothership 1242 does not Exist"
        }
        }
    ),    
}

mothership_add_ship_response_schema = {
    "201": openapi.Response(
        description="Add Ships to a Mothership",
        examples={
            "application/json": {
            "msg": "1 ships added"
        }
        }
    ),    
    "400": openapi.Response(
        description="Bad request",
        examples={
            "application/json": {
        "error": "The ship 5 does not have enough capacity"
        }
        }
    ),    
}

mothership_list_response_schema = {
    "200": openapi.Response(
        description="List all motherships",
        examples={"application/json":[
    {
        "id": 1,
        "name": "ZXS978",
        "capacity": 9
    },
    {
        "id": 2,
        "name": "ZXS978",
        "capacity": 9
    }
    ]}
    ),
    "404": openapi.Response(
        description="Error",
        examples={
            "application/json": {
        "error": "Ship does not Exist"
        }
        }
    ),
}

crew_create_response_schema = {
    "200": openapi.Response(
        description="Crew created",
        examples={
            "application/json": {
            "id": 12,
            "name": "test",
            "ship": 6
            }
        }
    ),
    "404": openapi.Response(
        description="Ship does not Exist",
        examples={
            "application/json": {
        "error": "Ship does not Exist"
        }
        }
    ),
}

crew_delete_response_schema = {
    "200": openapi.Response(
        description="Delete a crew member",
        examples={
            "application/json": {
            "msg": "Crew member 25 deleted"
            }
        }
    ),
    "400": openapi.Response(
        description="Crew does not Exist",
        examples={
            "application/json": {
        "error": "Crew 124 does not Exist"
        }
        }
    ),
}
    
crew_detail_response_schema = {
    "200": openapi.Response(
        description="Get details of a crew member",
        examples={
            "application/json": {
            "id": 12,
            "name": "test",
            "ship": 6
            }
        }
    ),
    "400": openapi.Response(
        description="Crew does not Exist",
        examples={
            "application/json": {
        "error": "Crew 124 does not Exist"
        }
        }
    ),
}

crew_list_response_schema = {
    "200": openapi.Response(
        description="List all crew members",
        examples={"application/json":[
    {
        "id": 1,
        "name": "Christine Gray",
        "ship": 1
    },
    {
        "id": 2,
        "name": "Arthur Mcwilliams",
        "ship": 1
    }
    ]}
    ),
    "404": openapi.Response(
        description="Error",
        examples={
            "application/json": {
        "error": "Ship does not Exist"
        }
        }
    ),
}

ship_list_response_schema = {
    "200": openapi.Response(
        description="List all motherships",
        examples={"application/json":[
        {
        "id": 1,
        "alias": "ship_XTMC",
        "capacity": 5,
        "mothership": 1
        },
        {
        "id": 2,
        "alias": "ship_HSVO",
        "capacity": 5,
        "mothership": 1
        }
    ]}
    ),
    "404": openapi.Response(
        description="Error",
        examples={
            "application/json": {
        "error": "Ship does not Exist"
        }
        }
    ),
}

ship_create_response_schema = {
    "200": openapi.Response(
        description="Mothership created",
        examples={
            "application/json": {
            "id": 15,
            "alias": "ship_HSVO",
            "capacity": 5,
            "mothership": 2
            }
        }
    ),
    "400": openapi.Response(
        description="Bad request",
        examples={
            "application/json": {
        "error": "Mothership does not Exist"
        }
        }
    ),
}

ship_add_member_response_schema = {
    "200": openapi.Response(
        description="Mothership created",
        examples={
            "application/json": {
            "id": 40,
            "name": "Luther",
            "ship": 2
            }
        }
    ),
    "404": openapi.Response(
        description="Bad request",
        examples={
            "application/json": {
        "error": "Ship 235532 does not exist"
        }
        }
    ),
}

ship_switch_member_response_schema = {
    "200": openapi.Response(
        description="Mothership created",
        examples={
            "application/json": {
            "msg": "Crew member switched"
            }
        }
    ),
    "400": openapi.Response(
        description="Bad request",
        examples={
            "application/json": {
        "error": "Crew member Paula Fernandes is not on the ship 1"
        }
        }
    ),
}

ship_detail_response_schema = {
    "200": openapi.Response(
        description="",
        examples={
            "application/json": {
            "id": 8,
            "alias": "ship_XTTS",
            "capacity": 5,
            "mothership": 3
        }
        }
    ),    
    "400": openapi.Response(
        description="Bad request",
        examples={
            "application/json": {
        "error": "Ship 83 does not Exist"
        }
        }
    ),    
}

ship_delete_response_schema = {
    "200": openapi.Response(
        description="",
        examples={
            "application/json": {
            "msg": "Ship 2 deleted"
        }
        }
    ),    
    "400": openapi.Response(
        description="Bad request",
        examples={
            "application/json": {
        "error": "Ship 83 does not Exist"
        }
        }
    ),    
}