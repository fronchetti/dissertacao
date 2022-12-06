install.packages("ScottKnottESD")
library(ScottKnottESD)

# Data reading & Scott Knott calculation
# CT - Choose the task
CT <- read.csv("~/GitHub/ICSE-2023/results/feature_analysis/CT.csv", row.names=1)
sk_CT <- sk_esd(CT)
# CF - Contribution Flow
CF <- read.csv("~/GitHub/ICSE-2023/results/feature_analysis/CF.csv", row.names=1)
sk_CF <- sk_esd(CF)
# Build local workspace
BW <- read.csv("~/GitHub/ICSE-2023/results/feature_analysis/BW.csv", row.names=1)
sk_BW <- sk_esd(BW)
# TC - Talk to the community
TC <- read.csv("~/GitHub/ICSE-2023/results/feature_analysis/TC.csv", row.names=1)
sk_TC <- sk_esd(TC)
# NC - No categories identified
NC <- read.csv("~/GitHub/ICSE-2023/results/feature_analysis/NC.csv", row.names=1)
sk_NC <- sk_esd(NC)
# SC - Submit the changes 
SC <- read.csv("~/GitHub/ICSE-2023/results/feature_analysis/SC.csv", row.names=1)
sk_SC <- sk_esd(SC)

# Image generation
# Size 7 x 12
# bottom, left, top, and right
par(mar=c(14, 12, 2, 12))
par(cex.axis=3, lwd=2) # y-ticks size

# CF - Contribution Flow
plot(sk_CF, col=c("#0F9D58", "#4285F4", "#a36a00", "#DB4437", "#AE00FF"), pch = 16, ylab="", xlab="", title="", cex=3, lwd = 3, padj=1, las=1, xaxt = "n", labels=FALSE)
axis(side = 1, labels = FALSE)
text(x = 1:length(sk_CF$groups),
     y = par("usr")[3] - 0.07,
     labels = names(sk_CF$groups),
     xpd = NA,
     srt = -20,
     col=c("#0F9D58", "#0F9D58", "#4285F4", "#4285F4", "#a36a00"),
     adj = 0,
     cex = 2.5)
mtext("Média", side=2, line=5, cex=3)
mtext("Características agrupadas por cor", side=1, line=2.5, cex=3, padj=5)

# CT - Choose the task
plot(sk_CT, col=c("#0F9D58", "#4285F4", "#a36a00", "#DB4437", "#AE00FF"), pch = 16, ylab="", xlab="", title="", cex=3, lwd = 3, padj=1, las=1, xaxt = "n", labels=FALSE)
axis(side = 1, labels = FALSE)
text(x = 1:length(sk_CT$groups),
     y = par("usr")[3] - 0.07,
     labels = names(sk_CT$groups),
     xpd = NA,
     srt = -20,
     col=c("#0F9D58", "#4285F4", "#4285F4", "#a36a00", "#a36a00"),
     adj = 0,
     cex = 2.5)
mtext("Média", side=2, line=5, cex=3)
mtext("Características agrupadas por cor", side=1, line=2.5, cex=3, padj=5)


# Build local workspace
plot(sk_BW, col=c("#0F9D58", "#4285F4", "#a36a00", "#DB4437", "#AE00FF"), pch = 16, ylab="", xlab="", title="", cex=3, lwd = 3, padj=1, las=1, xaxt = "n", labels=FALSE)
axis(side = 1, labels = FALSE)
text(x = 1:length(sk_BW$groups),
     y = par("usr")[3] - 0.07,
     labels = names(sk_BW$groups),
     xpd = NA,
     srt = -20,
     col=c("#0F9D58", "#4285F4", "#4285F4", "#a36a00", "#a36a00"),
     adj = 0,
     cex = 2.5)
mtext("Média", side=2, line=5, cex=3)
mtext("Média", side=2, line=5, cex=3)
mtext("Características agrupadas por cor", side=1, line=2.5, cex=3, padj=5)

# TC - Talk to the community
plot(sk_TC, col=c("#0F9D58", "#4285F4", "#a36a00", "#DB4437", "#AE00FF"), pch = 16, ylab="", xlab="", title="", cex=3, lwd = 3, padj=1, las=1, xaxt = "n", labels=FALSE)
mtext("Média", side=2, line=5, cex=3)
mtext("Características agrupadas por cor", side=1, line=2.5, cex=3, padj=5)

# DC - Deal with the code
DC <- read.csv("~/GitHub/ICSE-2023/results/feature_analysis/DC.csv", row.names=1)
sk_DC <- sk_esd(DC)
plot(sk_DC, col=c("#0F9D58", "#4285F4", "#a36a00", "#DB4437", "#AE00FF"), pch = 16, ylab="", xlab="", title="", cex=3, lwd = 3, padj=1, las=1, xaxt = "n", labels=FALSE)
mtext("Média", side=2, line=5, cex=3)
mtext("Características agrupadas por cor", side=1, line=2.5, cex=3, padj=5)

# NC - No categories identified
plot(sk_NC, col=c("#0F9D58", "#4285F4", "#a36a00", "#DB4437", "#AE00FF"), pch = 16, ylab="", xlab="", title="", cex=3, lwd = 3, padj=1, las=1, xaxt = "n", labels=FALSE)
mtext("Média", side=2, line=5, cex=3)
mtext("Características agrupadas por cor", side=1, line=2.5, cex=3, padj=5)

# SC - Submit the changes
plot(sk_SC, col=c("#0F9D58", "#4285F4", "#a36a00", "#DB4437", "#AE00FF"), pch = 16, ylab="", xlab="", title="", cex=3, lwd = 3, padj=1, las=1, xaxt = "n", labels=FALSE, ylim=c(2, 3.1))
mtext("Média", side=2, line=5, cex=3)
mtext("Características agrupadas por cor", side=1, line=2.5, cex=3, padj=5)
