import matplotlib.pyplot as plt

# Extract broadband subscriptions data
broadband_subscriptions = [150, 100, 75, 50, 35, 25, 15]

# Create a histogram
plt.hist(broadband_subscriptions, bins=10, edgecolor='black')

# Set labels and title
plt.xlabel('Broadband subscriptions')
plt.ylabel('Number of entities')
plt.title('Distribution of broadband subscriptions')

# Show the plot
plt.show()