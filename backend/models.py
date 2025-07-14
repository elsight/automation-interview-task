from pydantic import BaseModel, IPvAnyAddress, Field, field_validator
from typing import Annotated

class Device(BaseModel):
    name: str = Field(..., min_length=1, description="Name of the device")
    ip_address: Annotated[
        IPvAnyAddress,
        Field(description="Valid IPv4 or IPv6 address (e.g., '192.168.1.1' or '2001:db8::1')")
    ]

    @field_validator('ip_address', mode='before')
    @classmethod
    def validate_ip(cls, v):
        if not isinstance(v, str):
            return v
        v = v.strip()
        if not v:
            raise ValueError("IP address cannot be empty")
        if not any(c.isdigit() for c in v):
            raise ValueError("IP address must contain at least one number")
        # Additional validation to provide a more user-friendly message
        if not ('.' in v or ':' in v):
            raise ValueError("Invalid IP address format. Must be a valid IPv4 (like 192.168.1.1) or IPv6 address")
        return v