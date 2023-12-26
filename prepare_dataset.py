def prepare_dataset(test_size=0.2, random_seed=1):
    dataset = pd.read_csv(
        "winequality-red.csv",
        delimiter=",",
    )
    dataset = dataset.rename(columns=lambda x: x.lower().replace(" ", "_"))
    train_df, test_df = train_test_split(dataset, test_size=test_size, random_state=random_seed)
    return {"train": train_df, "test": test_df}