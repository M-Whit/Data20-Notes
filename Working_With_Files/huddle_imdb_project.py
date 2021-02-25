import csv


class imdb:

    # Initialise the class, with temporary tables for later use
    def __init__(self):
        self.csvfile = ''
        self.header = [['Title Type', 'Title', 'Start Year', 'Runtime (Mins)', 'Genre']]
        self.csv_read = []
        self.movies_shows = []

    # Extracts csv file into Python, minus the column headers
    def extraction(self):
        with open(self.csvfile) as file:
            readcsv = csv.reader(file, delimiter=',')
            next(readcsv)
            self.csv_read = list(readcsv)
            return self.csv_read

    # Return only movie and tvSeries
    def movies_and_shows(self):
        for i in self.csv_read:
            if i[0] == 'movie' or i[0] == 'tvSeries':
                self.movies_shows.append(i)
        return self.movies_shows

    # Remove secondary genres from remaining entries
    def remove_secondary_genres(self):
        for i in self.movies_shows:
            # Split the entries by their delimiter and return the primary genre
            i[7] = i[7].split(',', 1)[0]
        return self.movies_shows

    # Remove the end year, is adult, and original title columns
    def remove_columns(self):
        for i in self.movies_shows:
            # Pop the unwanted columns for each row
            i.pop(5)
            i.pop(3)
            i.pop(2)
        return self.movies_shows

    # Loading the transformed data into a new csv file
    def loading_csv(self, new_file_name):
        # Joining self.header and self.movies_shows
        self.header.extend(self.movies_shows)

        with open(new_file_name, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(self.header)


# Define the main function to run all previously defined methods
def main(old_file_name, new_file_name):
    # Creating an instance of imdb()
    example = imdb()
    example.csvfile = old_file_name
    # Extracting and transforming data
    example.extraction()
    example.movies_and_shows()
    example.remove_secondary_genres()
    example.remove_columns()
    example.loading_csv(new_file_name)


# Run the main function
main("imdbtitles.csv", "new_imdb_titles.csv")

