from commonWorkflow import ocrCropGetString, AdbClick

nextTicketTime = ocrCropGetString(0.70, 0.88, 0.85, 0.93)[-1]
topOpponentHardness = ocrCropGetString(0.70, 0.50, 0.82, 0.54)[-1]
downOpponentHardness = ocrCropGetString(0.70, 0.79, 0.82, 0.83)[-1]
ticketAvailable = ocrCropGetString(0.64, 0.88, 0.68, 0.93)[-1]


1810, 342
if ticketAvailable > 0:
    # Swap ennemy
    AdbClick(94, 31)
    AdbClick(94, 61)