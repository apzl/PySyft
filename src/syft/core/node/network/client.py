# external class imports
from typing import List
from typing import Optional
from typing_extensions import final

# syft imports
from ...io.location import SpecificLocation
from ....decorators import syft_decorator
from ...io.location import Location
from ..common.client import Client
from ...common.uid import UID
from ...io.route import Route


@final
class NetworkClient(Client):

    network: SpecificLocation  # redefine the type of self.vm to not be optional

    @syft_decorator(typechecking=True)
    def __init__(
        self,
        name: str,
        routes: List[Route],
        network: SpecificLocation,
        domain: Optional[Location] = None,
        device: Optional[Location] = None,
        vm: Optional[Location] = None,
    ):
        super().__init__(
            name=name,
            routes=routes,
            network=network,
            domain=domain,
            device=device,
            vm=vm,
        )

    @property
    def id(self) -> UID:
        return self.network.id

    @property
    def domain(self) -> Optional[Location]:
        """This client points to a node, if that node lives within a domain
        or is a domain itself, this property will return the Location of that domain
        if it is known by the client."""

        return super().domain

    @domain.setter
    def domain(self, new_domain: Location) -> Optional[Location]:
        """This client points to a node, if that node lives within a domain
        or is a domain itself and we learn the Location of that domain, this setter
        allows us to save the Location of that domain for use later. We use a getter
        (@property) and setter (@set) explicitly because we want all clients
        to efficiently save an address object for use when sending messages to their
        target. That address object will include this information if it is available"""

        raise Exception(
            "This client points to a network, you don't need a Domain Location."
        )

    @property
    def device(self) -> Optional[Location]:
        """This client points to a node, if that node lives within a device
        or is a device itself, this property will return the Location of that device
        if it is known by the client."""

        return super().device

    @device.setter
    def device(self, new_device: Location) -> Optional[Location]:
        """This client points to a node, if that node lives within a device
        or is a device itself and we learn the Location of that device, this setter
        allows us to save the Location of that device for use later. We use a getter
        (@property) and setter (@set) explicitly because we want all clients
        to efficiently save an address object for use when sending messages to their
        target. That address object will include this information if it is available"""

        raise Exception(
            "This client points to a network, you don't need a Device Location."
        )

    @property
    def vm(self) -> Optional[Location]:
        """This client points to an node, if that node lives within a vm
        or is a vm itself, this property will return the Location of that vm
        if it is known by the client."""

        return super().vm

    @vm.setter
    def vm(self, new_vm: Location) -> Optional[Location]:
        """This client points to an node, if that node lives within a vm
        or is a vm itself and we learn the Location of that vm, this setter
        allows us to save the Location of that vm for use later. We use a getter
        (@property) and setter (@set) explicitly because we want all clients
        to efficiently save an address object for use when sending messages to their
        target. That address object will include this information if it is available"""

        raise Exception(
            "This client points to a network, you don't need a VM Location."
        )

    @syft_decorator(typechecking=True)
    def __repr__(self) -> str:
        out = f"<Network:{self.name}>"
        return out