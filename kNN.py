#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[47]:


def knn(data, query, k, distance_fn, choice_fn):
    neighbor_distances_and_indices = [] 
    
    # 3. For each example in the data
    for index, example in enumerate(data):
        # 3.1 Calculate the distance between the query example and the current
        # example from the data.
        distance = distance_fn(example[:-1], query)
        
        # 3.2 Add the distance and the index of the example to an ordered collection
        neighbor_distances_and_indices.append((distance, index))
    
    # 4. Sort the ordered collection of distances and indices from
    # smallest to largest (in ascending order) by the distances
    sorted_neighbor_distances_and_indices = sorted(neighbor_distances_and_indices)
    
    # 5. Pick the first K entries from the sorted collection
    k_nearest_distances_and_indices = sorted_neighbor_distances_and_indices[:k]
    
    # 6. Get the labels of the selected K entries
    k_nearest_labels = [data[i][-1] for distance, i in k_nearest_distances_and_indices]

    # 7. If regression (choice_fn = mean), return the average of the K labels
    # 8. If classification (choice_fn = mode), return the mode of the K labels
    return k_nearest_distances_and_indices , choice_fn(k_nearest_labels)


# In[48]:



def mean(labels):
    return sum(labels) / len(labels)

def mode(labels):
    return Counter(labels).most_common(1)[0][0]

def euclidean_distance(point1, point2):
    sum_squared_distance = 0
    for i in range(len(point1)):
        sum_squared_distance += math.pow(point1[i] - point2[i], 2)
    return math.sqrt(sum_squared_distance)


# In[49]:


def recommend_fruits(fruit_query, k_recommendations):
    raw_fruit_data = []
    with open('fruit_data_with_colors(1).csv', 'r') as md:
        # Discard the first line (headings)
        next(md)

        # Read the data into memory
        for line in md.readlines():
#             print(line)
            data_row = line.strip().split(',')
#             print(data_row)
            data_row = ['Nan' if x == '' else x for x in data_row]
            raw_fruit_data.append(data_row)

    
    # Prepare the data for use in the knn algorithm by picking
    # the relevant columns and converting the numeric columns
    # to numbers since they were read in as strings
    
    fruits_recommendation_data = []
    for row in raw_fruit_data:
        data_row = list(map(float, row[3:]))       # I don't need ist 2 column
        fruits_recommendation_data.append(data_row)

    # Use the KNN algorithm to get the 3 fruits that are most
    # similar to The Post.
#     print(fruits_recommendation_data)
    recommendation_indices, _ = knn(
        fruits_recommendation_data, fruit_query, k=k_recommendations,
        distance_fn=euclidean_distance, choice_fn=lambda x: None
    )

    fruit_recommendations = []
    for _, index in recommendation_indices:
        fruit_recommendations.append(raw_fruit_data[index])

    return fruit_recommendations


# In[50]:



if __name__ == '__main__':
    the_post = [199,8.23, 3.1, 1.35]# feature vector for The Post
    recommended_fruits = recommend_fruits(fruit_query=the_post, k_recommendations=3)

    # Print recommended fruit titles
    for recommendation in recommended_fruits:
        print(recommendation[1])


# In[ ]:





# In[ ]:





# In[ ]:




