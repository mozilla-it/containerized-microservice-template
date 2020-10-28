import json
from jinja2 import Environment, select_autoescape
import json

import jinja2
from behave import then, when, step
from jinja2 import Environment, select_autoescape

from tests.bdd.steps.parent_step import ParentStep


class BddExampleSteps(ParentStep):
    @when("we do an operation with a context table")
    def operation_with_context_table(self):
        self.param_dict = dict()
        for row in self.table:
            key = row["key"]
            value = row["value"]
            self.param_dict.update({key: value})

        file_key = "example_file"
        if file_key in self.param_dict.keys():
            self.file = self.param_dict.get(file_key)

        self.result = self.param_dict

    @step("we input the template items in the file")
    def input_template(self):
        env = Environment(
            loader=jinja2.FileSystemLoader(self.path),
            autoescape=select_autoescape(["json"]),
        )
        env.filters["jsonify"] = json.dumps
        common_template = env.get_template(self.file)
        render = common_template.render(page=self.param_dict)

        self.result = json.loads(render)

    @then("result should be the following table")
    def result_check_on_table(self):
        for row in self.table:
            key = row["key"]
            value = row["value"]
            if "num" in key:
                value = float(value)
            assert key in self.result.keys(), f"The key was not found:{key}"
            assert (
                self.result[key] == value
            ), f"The key was not associated with the expected value:{key}"
