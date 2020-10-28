# Created by bsieber
Feature: Behave Example Test

  Scenario: Example using context table
    Given a path to our resources tests/resources/bdd_example_files/
    When we do an operation with a context table
      | key           | value           |
      | EXAMPLE_KEY_1 | example_key     |
      | EXAMPLE_KEY_2 | example_channel |
    Then result should be the following table
      | key           | value           |
      | EXAMPLE_KEY_1 | example_key     |
      | EXAMPLE_KEY_2 | example_channel |

  Scenario: Example using a template and replacing values
    Given a path to our resources tests/resources/bdd_example_files/
    When we do an operation with a context table
      | key           | value             |
      | EXAMPLE_KEY_1 | example_key       |
      | EXAMPLE_KEY_2 | example_channel   |
      | example_file  | example_file.json |
    When we input the template items in the file
    Then result should be the following table
      | key         | value             |
      | key_1       | example_key       |
      | key_2       | example_channel   |
      | file_key    | example_file.json |
      | example_num | 0.8               |
