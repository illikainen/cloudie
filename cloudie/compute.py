import click
from libcloud.common.base import BaseDriver
from libcloud.compute.providers import Provider

from . import cloud, table


@click.group()
def compute() -> None:
    pass


@compute.command("list-images")
@cloud.pass_driver(Provider)
def list_images(driver: BaseDriver) -> None:
    table.show([
        ["ID", "id"],
        ["Name", "name"],
    ], driver.list_images())