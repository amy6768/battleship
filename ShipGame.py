# Name: Amy Lee
# Course: CS162

# HALFWAY PROGRESS REPORT

# I am writing class called ShipGame. Within this class is
# code that allows two people to play the classic game
# of Battleship.

class ShipGame:
    """
    The ShipGame class allows two people to play the
    game of Battleship. Each player has their own grid
    that is 10x10 in size. They place their ships on
    the grid and take turns firing torpedoes at their
    enemy's grid. The first torpedo is fired by
    'first' player. A ship is considered sunk when
    all of its squares on the grid have been hit.
    Whoever sinks all of their opponent's ships
    is the winner of the game.
    """

    def __init__(self):
        """
        The constructor for the ShipGame class. Takes no
        parameters. Sets all data members to their initial
        values

        Data members:
        first_player_board - initializes empty list that will hold ships for first player
        second_player_board - initializes empty list that will hold ships for second player
        current_state - initializes to 'UNFINISHED'
        players_turn - initializes to 'first'

        """
        self._first_player_board = []
        self._second_player_board = []
        self._current_state = 'UNFINISHED'
        self._players_turn = 'first'

    def get_first_player_board(self):
        """
        Returns the first player's board
        """

        return self._first_player_board

    def get_second_player_board(self):
        """
        Returns the second player's board
        """

        return self._second_player_board

    def get_players_turn(self):
        """
        Returns which player's turn it is
        """

        return self._players_turn

    def place_ship(self, player, ship_length, coord, orientation):
        """
        Takes four parameters:
        player - Represents either 'first' player or 'second' player
        ship_length - Represents the length of the ship being place on board
        coord - Represents the coordinate that the ship is going to occupy
        that is closet to A1
        orientation - Represents whether the ship is going to occupy the
        same row 'R' or if it's going to occupy the same column 'C'

        Purpose:
        The purpose of this method is to place a ship on the 10x10
        grid. Before the ship is placed on board, the following things must
        be checked: if the ship fits entirely on the 10x10 grid, if it
        overlaps with a previously placed ship, or if the length of the
        ship is less than 2. If something does not check out, the method
        returns False, and the ship is not placed. If everything does check
        out okay, the ship is placed on the player's grid and the method
        returns True. This method will update either the first_player_board
        or the second_player_board.

        Returns:

        False - ship can not be placed on the board after criteria is checked

        True - ship is placed on board after criteria is checked

        """

        # Check first player board
        if player == 'first':
            col_num = ''
            dict_of_values = {}
            # Check to see if ship is longer than
            # the board or if the ship is too short
            if ship_length > 10 or ship_length < 2:
                return False
            # Checking to see if ship fits entirely
            # on the board
            if orientation == 'R':
                if len(coord) == 2:
                    col_num = coord[1]
                    if (int(col_num) + ship_length) > 11:
                        return False
                elif len(coord) == 3:
                    if coord[1] == 1 and coord[2] == 0:
                        col_num = 10
                        if col_num + ship_length > 11:
                            return False
            if orientation == 'C':
                dict_of_values = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10}
                row_num = coord[0]
                if row_num in dict_of_values:
                    value = dict_of_values.get(row_num)
                    if value + ship_length > 11:
                        return False

            # Check for overlap using coordinate
            for ship in self._first_player_board:
                for ship_coord in ship:
                    if coord == ship_coord:
                        return False

            # Check for overlap using other coordinates
            # based on ship_length and ship orientation
            # as column
            if orientation == 'C':
                coord_to_check = [coord]
                counter = ship_length - 1
                letter = coord[0]
                temp_letter = letter
                digit_to_nine = coord[1]
                if len(coord) == 3:
                    digit_ten = coord[1] + coord[2]
                if len(coord) == 2:
                    while counter > 0:
                        temp_letter = chr(ord(temp_letter) + 1)
                        check_coord = temp_letter + digit_to_nine
                        coord_to_check.append(check_coord)
                        counter -= 1
                if len(coord) == 3:
                    while counter > 0:
                        temp_letter = chr(ord(letter) + 1)
                        check_coord = temp_letter + digit_ten
                        coord_to_check.append(check_coord)
                        counter -= 1
                # Check each coordinate in first player board
                # for overlaps
                for coord in coord_to_check:
                    for ship in self._first_player_board:
                        for element in ship:
                            if coord == element:
                                return False

            # Check for overlap using other coordinates
            # based on ship_length and ship orientation
            # as row
            if orientation == 'R':
                coord_to_check = [coord]
                counter = ship_length - 1
                letter = coord[0]
                number = coord[1]
                temp_number = number
                digit_to_nine = coord[1]
                if len(coord) == 3:
                    digit_ten = coord[1] + coord[2]
                if len(coord) == 2:
                    while counter > 0:
                        temp_number = int(temp_number) + 1
                        check_coord = letter + str(temp_number)
                        coord_to_check.append(check_coord)
                        counter -= 1
                if len(coord) == 3:
                    while counter > 0:
                        temp_number = int(temp_number) + 1
                        check_coord = letter + str(temp_number)
                        coord_to_check.append(check_coord)
                        counter -= 1
                # Check each coordinate in first player board
                # for overlaps
                for coord in coord_to_check:
                    for ship in self._first_player_board:
                        for element in ship:
                            if coord == element:
                                return False

            # Add ship to first player board
            self._first_player_board.append(coord_to_check)
            print(self._first_player_board)
            return True

        # Check second player board
        if player == 'second':
            col_num = ''
            dict_of_values = {}
            # Check to see if ship is longer than
            # the board or if the ship is too short
            if ship_length > 10 or ship_length < 2:
                return False
            # Checking to see if ship fits entirely
            # on the board
            if orientation == 'R':
                if len(coord) == 2:
                    col_num = coord[1]
                    if (int(col_num) + ship_length) > 11:
                        return False
                elif len(coord) == 3:
                    if coord[1] == 1 and coord[2] == 0:
                        col_num = 10
                        if col_num + ship_length > 11:
                            return False
            if orientation == 'C':
                dict_of_values = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}
                row_num = coord[0]
                if row_num in dict_of_values:
                    value = dict_of_values.get(row_num)
                    if value + ship_length > 11:
                        return False

        # Check for overlap
            for ship in self._second_player_board:
                for ship_coord in ship:
                    if coord == ship_coord:
                        return False

        # Check for overlap using other coordinates
        # based on ship_length
            if orientation == 'C':
                coord_to_check = [coord]
                counter = ship_length - 1
                letter = coord[0]
                digit_to_nine = coord[1]
                temp_letter = letter
                if len(coord) == 3:
                    digit_ten = coord[1] + coord[2]
                if len(coord) == 2:
                    while counter > 0:
                        temp_letter = chr(ord(temp_letter) + 1)
                        check_coord = temp_letter + digit_to_nine
                        coord_to_check.append(check_coord)
                        counter -= 1
                if len(coord) == 3:
                    while counter > 0:
                        temp_letter = chr(ord(letter) + 1)
                        check_coord = temp_letter + digit_ten
                        coord_to_check.append(check_coord)
                        counter -= 1
                # Check each coordinate in first player board
                # for overlaps
                for coord in coord_to_check:
                    for ship in self._second_player_board:
                        for element in ship:
                            if coord == element:
                                return False

            # Check for overlap using other coordinates
            # based on ship_length and ship orientation
            # as row
            if orientation == 'R':
                coord_to_check = [coord]
                counter = ship_length - 1
                letter = coord[0]
                number = coord[1]
                temp_number = number
                digit_to_nine = coord[1]
                if len(coord) == 3:
                    digit_ten = coord[1] + coord[2]
                if len(coord) == 2:
                    while counter > 0:
                        temp_number = int(temp_number) + 1
                        check_coord = letter + str(temp_number)
                        coord_to_check.append(check_coord)
                        counter -= 1
                if len(coord) == 3:
                    while counter > 0:
                        temp_number = int(temp_number) + 1
                        check_coord = letter + str(temp_number)
                        coord_to_check.append(check_coord)
                        counter -= 1
            # Add ship to second player board
            self._second_player_board.append(coord_to_check)
            print(self._second_player_board)
            return True

    def get_current_state(self):
        """
        Takes no parameters

        Purpose:
        The purpose of this method is to tell user whether the first player won,
        the second player won, or if the game is unfinished.

        Returns:
       'FIRST_WON' - returns this string if first player won the game

       'SECOND_WON' - returns this string if second player won the game

       'UNFINISHED' - returns this string if the game is unfinished

        """
        return self._current_state

    def fire_torpedo(self, player, coord,):
        """
        Takes these parameters:
        player - takes in either 'first' or 'second' that shows who is
        firing the torpedo
        coord - takes in a coordinate that is the target square

        Purpose:
        The purpose of this method is to record a torpedo that has been
        fired. The method will return false and not record the torpedo
        if the game has already been won or if it's not that player's turn.
        Else, the torpedo will be fired and the following will be
        updated: record the move, update who turn it is, update the current
        state of the game. This method will update current_state when either
        one of the players win.

        Returns:
        False - if torpedo move is not recorded

        True - if torpedo is fired and recorded
        """
        # Check to see if correct player turn
        print("Players turn is: " + self.get_players_turn())
        if player != self.get_players_turn():
            return False

        if self.get_current_state() == 'FIRST_WON':
            return False

        if self.get_current_state() == 'SECOND_WON':
            return False

        # Check to see if coord is in second player board
        if player == 'first':
            element_counter_one = 0
            element_counter_two = 0
            for ship in self._second_player_board:
                for ship_coord in ship:
                    if coord == ship_coord:
                        del self._second_player_board[element_counter_one][element_counter_two]
                        self._players_turn = 'second'
                        if len(self._second_player_board) == 0:
                            self._current_state = 'FIRST_WON'
                        return True
                    element_counter_two += 1
                element_counter_one += 1


        # Check to see if coord is in first player board
        if player == 'second':
            element_counter_one = 0
            element_counter_two = 0
            for ship in self._first_player_board:
                for ship_coord in ship:
                    if coord == ship_coord:
                        del self._first_player_board[element_counter_one][element_counter_two]
                        self._players_turn = 'first'
                        if len(self._first_player_board) == 0:
                            self._current_state = 'SECOND_WON'
                        return True
                    element_counter_two += 1
                element_counter_one += 1

        return True


    def get_num_ships_remaining(self, player):
        """
        Takes in this parameter:
        player - an argument either 'first' or 'second'

        Purpose:
        The purpose of this method is to return how many ships are
        left on either the 'first' or 'second' player's 10x10 grid.
        This method will do a len() on either the first_player_board
        or the second_player_board to determine how many ships
        are remaining.

        Returns:
        Returns the number of ships that are left on the specified
        player's grid
        """
        if player == 'first':
            return len(self._first_player_board)

        if player == 'second':
            return len(self._second_player_board)

def main():

    game = ShipGame()
    print(game.place_ship('first', 5, 'B2', 'C'))
    print(game.place_ship('first', 2, 'I8', 'R'))
    print(game.place_ship('second', 3, 'H2', 'C'))
    print(game.place_ship('second', 2, 'A1', 'C'))
    print(game.place_ship('first', 8, 'H2', 'R'))
    print(game.get_second_player_board())
    print(game.fire_torpedo('first', 'H3'))
    print("before torpedo attempt: " + str(game.get_second_player_board()))
    #print(game.fire_torpedo('second', 'A1'))
    print(game.get_current_state())

if __name__ == '__main__':
    main()