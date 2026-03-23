from __future__ import annotations

from phone_pipeline.utils.phone_utils import is_valid_phone, normalize_phone_to_e164


def test_normalize_phone_to_e164_for_local_mobile_number() -> None:
    assert normalize_phone_to_e164("300-123-4567") == "+573001234567"


def test_normalize_phone_to_e164_preserves_international_prefix() -> None:
    assert normalize_phone_to_e164("+57 301 999 8888") == "+573019998888"


def test_normalize_phone_to_e164_returns_none_for_invalid_phone() -> None:
    assert normalize_phone_to_e164("invalid_phone") is None


def test_is_valid_phone_matches_normalization_result() -> None:
    assert is_valid_phone("300-123-4567") is True
    assert is_valid_phone("invalid_phone") is False
