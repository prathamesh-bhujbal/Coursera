from behave import when, then

@when('I request the product by id {id}')
def step_impl(context, id):
    response = context.client.get(f'/products/{id}')
    context.response = response

@then('the result should be the product "{name}"')
def step_impl(context, name):
    json_data = context.response.json
    assert json_data['name'] == name

@when('I update the product with id {id} and set price to {price}')
def step_impl(context, id, price):
    context.client.put(f'/products/{id}', json={'price': price})

@when('I delete the product with id {id}')
def step_impl(context, id):
    context.client.delete(f'/products/{id}')
