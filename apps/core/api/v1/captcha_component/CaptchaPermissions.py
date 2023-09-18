from rest_access_policy import AccessPolicy

class CaptchaAccessPolicy(AccessPolicy):
    statements = [
        {
            "action": ["get_captcha", "verify_captcha", "verify_captcha_approbed"],
            "principal": "*",
            "effect": "allow",
            "condition": ["is_atenticated"]
        },
        {
            "action": ["retrieve"],
            "principal": "*",
            "effect": "allow",
            "condition": ["is_atenticated", "is_owner"]
        },
        {
            "action": ["destroy", "partial_update", "update"],
            "principal": ["*"],
            "effect": "allow",
            "condition": ["is_atenticated", "is_owner"]
        },
        {
            "action": ["create"],
            "principal": ["*"],
            "effect": "allow",
            "condition": ["is_atenticated"]
        }
    ]

    def is_atenticated(self, request, view, action) -> bool:
        return request.user.is_authenticated

    def is_owner(self, request, view, action) -> bool:
        object = view.get_object()
        return request.user.id == int(object.pk)