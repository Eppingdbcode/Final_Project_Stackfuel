def main() -> None:
    """Run the table-building pipeline without importing it at package load."""
    from .pipeline import main as run_pipeline

    run_pipeline()

__all__ = ["main"]
