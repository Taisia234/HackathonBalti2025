# auth.py
from permguard.az.azreq.builder_principal import PrincipalBuilder
from permguard.az.azreq.builder_request_atomic import AZAtomicRequestBuilder
from permguard.az_client import AZClient
from permguard.az_config import with_endpoint
from users import USERS

az_client = AZClient(with_endpoint("localhost", 9094))

def is_authorized(email, action, resource_id="post"):
    user = USERS.get(email)
    if not user:
        return False, "User not found"

    principal = PrincipalBuilder(email).build()

    entities = [
        {
            "uid": {"type": "TNTSocial::Platform::Post", "id": resource_id},
            "attrs": {"active": True},
            "parents": [],
        }
    ]

    req = (
        AZAtomicRequestBuilder(
            245829639912,
            "33c9ff3eb77e4e1597410014b8449abc",
            user["role"],
            "TNTSocial::Platform::Post",
            f"TNTSocial::Platform::Action::{action}",
        )
        .with_request_id("1234")
        .with_principal(principal)
        .with_entities_items("cedar", entities)
        .with_subject_role_actor_type()
        .with_subject_source("keycloack")
        .with_subject_property("isSuperUser", user["isSuperUser"])
        .with_resource_id(resource_id)
        .with_resource_property("isEnabled", True)
        .with_action_property("isEnabled", True)
        .with_context_property("time", "2025-01-23T16:17:46+00:00")
        .with_context_property("isPostActive", True)
        .build()
    )

    ok, response = az_client.check(req)
    return ok, response
