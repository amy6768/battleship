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
        pass

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
        pass

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
        pass

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
        pass

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
        pass