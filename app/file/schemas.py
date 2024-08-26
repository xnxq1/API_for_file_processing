from pydantic import BaseModel, field_validator


class FileUpload(BaseModel):
    name: str
    format: str
    url: str

    @field_validator('url')
    @classmethod
    def validate_url(cls, url: str):
        if not url.startswith(('http://', 'https://')):
            raise ValueError('url должен начинаться с http://')
        return url


class SchemasFileForUser(BaseModel):
    name: str
    format: str
    size: int
    is_download: bool