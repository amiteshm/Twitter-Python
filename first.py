import twitter

api = twitter.Api(consumer_key='9uya1BgKAEJr7JHS1PgirA',
                           consumer_secret='3fakoGCco3Y0BMbLGbedlhlp5FL5eTDWellwmpI57u8',
                            access_token_key='241804566-h5jVW2k4pWdlb9vdaUOhVUc5SvylQsSTceANNXaA',
                            access_token_secret='QhpQw3rDx3N6npzAIc8wnsbTvNKIfJKXhh4FKSfSj8')

friends=api.PostUpdate("2nd tweet using python ")
