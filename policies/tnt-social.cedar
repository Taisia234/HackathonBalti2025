@id("platform-admin")
permit(
  principal == Permguard::IAM::RoleActor::"platform-admin",
  action in [ TNTSocial::Platform::Action::"view", TNTSocial::Platform::Action::"create", 
    TNTSocial::Platform::Action::"update", TNTSocial::Platform::Action::"delete"],
  resource is TNTSocial::Platform::Post
)
unless {
  principal has isSuperUser && principal.isSuperUser == false
};

@id("platform-moderator")
permit(
  principal == Permguard::IAM::RoleActor::"platform-moderator",
  action in [TNTSocial::Platform::Action::"view", TNTSocial::Platform::Action::"update", TNTSocial::Platform::Action::"delete"],
  resource is TNTSocial::Platform::Post
)
unless {
  principal has isSuperUser && principal.isSuperUser == false
};

@id("platform-viewer")
permit(
  principal == Permguard::IAM::RoleActor::"platform-viewer",
  action in [TNTSocial::Platform::Action::"view", TNTSocial::Platform::Action::"update"],
  resource is TNTSocial::Platform::Post
);

