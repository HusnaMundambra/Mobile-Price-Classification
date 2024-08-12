{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b50738cd-0c70-49af-ad6b-d068c2ec240a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "import pickle\n",
    "\n",
    "# Load the dataset\n",
    "mob_train = pd.read_csv('C:\\\\Users\\\\Husna\\\\Downloads\\\\mobile-aws\\\\train.csv')\n",
    "\n",
    "# Rename columns for easier handling\n",
    "train_mapper = {\n",
    "    \"four_g\": \"is4G\",\n",
    "    \"three_g\": \"is3G\",\n",
    "    \"mobile_wt\": \"mobile_weight\",\n",
    "    \"n_cores\": \"no_of_cores\",\n",
    "    \"sc_h\": \"screen_height\",\n",
    "    \"sc_w\": \"screen_width\",\n",
    "    \"int_memory\": \"internal_memory\",\n",
    "    \"pc\": \"primary_cam_MP\",\n",
    "    \"fc\": \"front_cam_MP\",\n",
    "    \"blue\": \"has_bluetooth\",\n",
    "    \"m_dep\": \"mobile_depth\"\n",
    "}\n",
    "mob_train.rename(columns=train_mapper, inplace=True)\n",
    "\n",
    "# Define features and target\n",
    "X = mob_train[['battery_power', 'px_height', 'px_width', 'ram', 'primary_cam_MP', 'front_cam_MP', 'screen_height']]\n",
    "y = mob_train['price_range']\n",
    "\n",
    "# Split the data into training and testing sets\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "# Train a RandomForest model\n",
    "model = RandomForestClassifier(random_state=42)\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "# Save the trained model as 'model.pkl'\n",
    "with open('model.pkl', 'wb') as model_file:\n",
    "    pickle.dump(model, model_file)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6804e622-aaf9-470f-8f74-d37debad6ceb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
