@id("platform-admin")
permit (
    principal,
    action,
    resource
)
when {
    principal.isAdmin == true &&
    context.hour >= 9 &&
    context.hour <= 20
};

@id("platform-power-user")
permit (
    principal,
    action in [Action::"Read", Action::"Write"],
    resource
)
when {
    principal.isPowerUser == true
};

@id("platform-user")
permit (
    principal,
    action in [Action::"Read"],
    resource is Resource::Record
);