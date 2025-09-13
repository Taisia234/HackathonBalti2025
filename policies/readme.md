n CLI (any folder):

1. permguard zones create --name magicfarmacia-dev
2. permguard authn tenants create --zone-id 396451458621 --name matera-branch
3. permguard authn identitysources create --zone-id 396451458621 --name google
4. permguard authz ledgers create --zone-id 396451458621 --name magicfarmacia

In repository:

1. permguard init --authz-language cedar
2. permguard remote add origin localhost
3. permguard checkout origin/396451458621/magicfarmacia
4. permguard validate
5. permguard plan
6. permguard apply
