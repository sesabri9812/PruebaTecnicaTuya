from __future__ import annotations

import re


COLOMBIA_COUNTRY_CODE = "57"
LOCAL_MOBILE_LENGTH = 10


def digits_only(phone: str) -> str:
    return re.sub(r"\D+", "", phone or "")


def normalize_phone(phone: str) -> str:
    return digits_only(phone)


def normalize_phone_to_e164(phone: str, country_code: str = COLOMBIA_COUNTRY_CODE) -> str | None:
    digits = digits_only(phone)

    if not digits:
        return None

    if digits.startswith(country_code) and len(digits) == len(country_code) + LOCAL_MOBILE_LENGTH:
        return f"+{digits}"

    if len(digits) == LOCAL_MOBILE_LENGTH and digits.startswith("3"):
        return f"+{country_code}{digits}"

    return None


def to_e164(phone: str, country_code: str = COLOMBIA_COUNTRY_CODE) -> str | None:
    return normalize_phone_to_e164(phone, country_code)


def is_valid_phone(phone: str, country_code: str = COLOMBIA_COUNTRY_CODE) -> bool:
    return normalize_phone_to_e164(phone, country_code) is not None
