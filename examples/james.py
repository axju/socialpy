from socialpy.butler import James


post = {
    'title': 'test',
}
james = James(api_storage_kwargs={'filename': 'test.json'})
james.post(post)
