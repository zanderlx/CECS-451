            if row is not 0:
                if (row+1, col) not in self.track:
                    self.track.append((row+1, col))
                if (row+2, col) not in self.track:
                    self.track.append((row+2, col))
                if (row+3, col) not in self.track:
                    self.track.append((row+3, col))