from permguard.az.azreq.builder_principal import PrincipalBuilder
from permguard.az.azreq.builder_request_atomic import AZAtomicRequestBuilder
from permguard.az_client import AZClient
from permguard.az_config import with_endpoint


az_client = AZClient(with_endpoint("localhost", 9094))

principal = PrincipalBuilder("ivan.smith@gmail.com").build()

entities = [
    {
        "uid": {"type": "TNTSocial::Platform::Post", "id": "post"},
        "attrs": {"active": True},
        "parents": [],
    }
]

req = (
    AZAtomicRequestBuilder(
        245829639912,
        "33c9ff3eb77e4e1597410014b8449abc",
        "platform-moderator",
        "TNTSocial::Platform::Post",
        "TNTSocial::Platform::Action::delete",
    )
    .with_request_id("1234")
    .with_principal(principal)
    .with_entities_items("cedar", entities)
    .with_subject_role_actor_type()
    .with_subject_source("keycloack")
    .with_subject_property("isSuperUser", True)
    .with_resource_id("e3a786fd07e24bfa95ba4341d3695ae8")
    .with_resource_property("isEnabled", True)
    .with_action_property("isEnabled", True)
    .with_context_property("time", "2025-01-23T16:17:46+00:00")
    .with_context_property("isPostActive", True)
    .build()
)

ok, response = az_client.check(req)

if ok:
    print("✅ authorization permitted")
else:
    print("❌ authorization denied")
    if response and response.context:
        if response.context.reason_admin:
            print(f"-> reason admin: {response.context.reason_admin.message}")
        if response.context.reason_user:
            print(f"-> reason user: {response.context.reason_user.message}")
        for eval in response.evaluations:
            if eval.context and eval.context.reason_user:
                print(f"-> reason admin: {eval.context.reason_admin.message}")
                print(f"-> reason user: {eval.context.reason_user.message}")
    if response and response.evaluations:
        for eval in response.evaluations:
            if eval.context:
                if eval.context.reason_admin:
                    print(f"-> evaluation requestid {eval.request_id}: reason admin: {eval.context.reason_admin.message}")
                if eval.context.reason_user:
                    print(f"-> evaluation requestid {eval.request_id}: reason user: {eval.context.reason_user.message}")