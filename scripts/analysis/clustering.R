install.packages("clustMixType")
install.packages("wesanderson")
install.packages("factoextra")
library(cluster)
library(factoextra)
library(wesanderson)
library("clustMixType")

cluster_features <- read.csv("cluster_features.csv")
cluster_features$paragraph_0p = factor(cluster_features$paragraph_0p)
cluster_features$paragraph_25p = factor(cluster_features$paragraph_25p)
cluster_features$paragraph_75p = factor(cluster_features$paragraph_75p)
cluster_features$paragraph_100p = factor(cluster_features$paragraph_100p)

numerical_features = cluster_features[, c(0, 1, 2, 3, 4, 5, 6, 7)]

# K-means (only numerical features)
fviz_nbclust(numerical_features, kmeans, method = "wss")
set.seed(123)
km.res <- kmeans(numerical_features, 2, nstart = 25)
c1 <- numerical_features[km.res$cluster==1,]
c2 <- numerical_features[km.res$cluster==2,]
boxplot(c1$n_CF, c2$n_CF, outline = FALSE)
clprofiles(km.res, numerical_features, col = wes_palette("Royal1", 2, type = "continuous"))


# K-prototype - All features and instances
Es <- numeric(10)
for(i in 1:10){
  kpres <- kproto(cluster_features, k = i, nstart = 5)
  Es[i] <- kpres$tot.withinss
}
plot(1:10, Es, type = "b", ylab = "Objective Function", xlab = "# Clusters",
     main = "Scree Plot") # figure 2


kpres <- kproto(cluster_features, k = 3)
kpres

par(mfrow=c(2,2))
clprofiles(kpres, cluster_features, col = wes_palette("Royal1", 3, type = "continuous"))

# K-prototype - All features but instances where paragraphs are not no category identified.
selected_cluster_features = cluster_features[cluster_features$paragraph_0p != "No categories identified." & 
                                               cluster_features$paragraph_25p != "No categories identified." &
                                               cluster_features$paragraph_75p != "No categories identified." &
                                               cluster_features$paragraph_100p != "No categories identified.",]

Es <- numeric(10)
for(i in 1:10){
  kpres <- kproto(selected_cluster_features, k = i, nstart = 5)
  Es[i] <- kpres$tot.withinss
}
plot(1:10, Es, type = "b", ylab = "Objective Function", xlab = "# Clusters",
     main = "Scree Plot") 

kpres <- kproto(selected_cluster_features, k = 3)
kpres

par(mfrow=c(2,2))
clprofiles(kpres, selected_cluster_features, col = wes_palette("Royal1", 3, type = "continuous"))
