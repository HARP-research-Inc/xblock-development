"""TO-DO: Write a description of what this XBlock is."""

from importlib.resources import files

from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Scope, String
from xblockutils.studio_editable import StudioEditableXBlockMixin


class QuiverXBlock(XBlock):
    """
    TO-DO: Plan out both the exact functionality and the UI of the XBlock
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    quiver_url = String(
        help="Public URL for q.uiver.app",
        default="https://q.uiver.app/?q=",
        scope=Scope.content,
    )
    height = String(
        help="height of the iframe window",
        default="500px",
        scope=Scope.content,
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        return files(__package__).joinpath(path).read_text(encoding="utf-8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the QuiverXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/quiver.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/quiver.css"))
        frag.add_javascript(self.resource_string("static/js/src/quiver.js"))
        frag.initialize_js('QuiverXBlock')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("QuiverXBlock",
             """<quiver/>
             """),
            ("Multiple QuiverXBlock",
             """<vertical_demo>
                <quiver/>
                <quiver/>
                <quiver/>
                </vertical_demo>
             """),
        ]
