"""Pydantic models for 職務経歴書 data."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, field_validator


class Environment(BaseModel):
    """開発環境."""

    languages: list[str] = []
    os: list[str] = []
    db: list[str] = []
    frameworks: list[str] = []
    aws: list[str] = []
    azure: list[str] = []
    gcp: list[str] = []
    tools: list[str] = []
    other: list[str] = []


class _ProjectBase(BaseModel):
    """プロジェクト共通フィールド."""

    model_config = ConfigDict(extra="forbid")

    period: str
    industry: str = ""
    name: str
    environment: Environment = Environment()
    abbreviate_env: bool = False
    team_size: str = ""
    role: str = ""


class StandardProject(_ProjectBase):
    """標準パターン."""

    overview: str = ""
    phases: str = ""
    responsibilities: list[str] = []
    achievements: list[str] = []


class StarProject(_ProjectBase):
    """STAR法パターン."""

    situation: list[str]
    task: list[str]
    action: list[str]
    result: list[str]

    @field_validator("situation", "task", mode="before")
    @classmethod
    def _coerce_str_to_list(cls, v: str | list[str]) -> list[str]:
        if isinstance(v, str):
            return [v]
        return v


# Backward compatibility alias
Project = StandardProject


class _CompanyBase(BaseModel):
    """会社経歴の共通フィールド."""

    company: str
    period: str
    business: str = ""
    capital: str = ""
    revenue: str = ""
    employees: str = ""
    listing: str = ""
    employment_type: str = ""
    job_type: str = ""
    other_activities: list[str] = []


class StandardCompany(_CompanyBase):
    """標準パターンの会社経歴."""

    projects: list[StandardProject] = []


class StarCompany(_CompanyBase):
    """STAR法パターンの会社経歴."""

    projects: list[StarProject] = []


# Backward compatibility alias
Company = StandardCompany


class SideProject(BaseModel):
    """副業・その他経歴のプロジェクト."""

    model_config = ConfigDict(extra="forbid")

    period: str
    name: str
    description: list[str] = []
    environment: Environment = Environment()
    abbreviate_env: bool = False
    team_size: str = ""
    role: str = ""

    @field_validator("description", mode="before")
    @classmethod
    def _coerce_str_to_list(cls, v: str | list[str]) -> list[str]:
        if isinstance(v, str):
            return [v]
        return v


class SideCompany(BaseModel):
    """副業・その他経歴の会社."""

    company: str
    period: str
    employment_type: str = ""
    job_type: str = ""
    projects: list[SideProject] = []


class SkillItem(BaseModel):
    """スキル項目."""

    name: str
    period: str = ""
    level: str = ""


class SkillCategory(BaseModel):
    """スキルカテゴリ."""

    category: str
    items: list[SkillItem]


class Qualification(BaseModel):
    """資格."""

    name: str
    date: str = ""


class SelfPRSection(BaseModel):
    """自己PRセクション."""

    title: str
    content: str


class _WorkHistoryBase(BaseModel):
    """職務経歴書の共通フィールド."""

    date: str
    name: str
    summary: str = ""
    highlights: list[str] = []
    side_experience: list[SideCompany] = []
    technical_skills: list[SkillCategory] = []
    qualifications: list[Qualification] = []
    self_pr: list[SelfPRSection] = []


class StandardWorkHistory(_WorkHistoryBase):
    """標準パターンの職務経歴書."""

    experience: list[StandardCompany] = []


class StarWorkHistory(_WorkHistoryBase):
    """STAR法パターンの職務経歴書."""

    experience: list[StarCompany] = []


# Backward compatibility alias
WorkHistory = StandardWorkHistory
