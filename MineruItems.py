import logging
import asyncio

from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)

# ./bdaddr -i hci0 94:58:CB:AF:53:48
# hciconfig hci0 reset
# systemctl restart bluetooth.service

# plugins/zelda-totk/AutoDupeMineru.py
# Required to be in menu and select the item to be duplicated
# Duplication keys: 
#   Enable add to hand: X down X up
#   Add to hand (Repeat 5 times): A down A up
#   Sort and exit simultaneously: Y down B down - wait 0.1s - Y up B up
#   Open menu: press + button

class AutoDupeMineru(JoycontrolPlugin):
    async def run(self):
        logger.info('Auto Dupe Mineru Plugin')
        # while True:
        #     line = input("press key to be relayed...")
        #     await self.button_push(line)

        
        # Press the A button when the controller is ready for input.
        logger.info('Pairing completed.')
        for i in range(3):
            logger.info('Press a for the {} time (of 5)'.format(i+1))
            await self.wait(0.5)
            await self.button_push('a')
            await self.wait(0.5)

        await self.button_push('plus')
        # Menu variant: use that instead of plus
        # await self.button_push('b')

        logger.info('Auto Dupe Mineru Plugin loaded!')

        while True:
            # Enable add to hand
            logger.info('Enable add to hand in 1 second')
            await self.wait(0.1)
            await self.button_push("x")
            await self.wait(0.1)

            # Add to hand (Repeat 5 times)
            for _ in range(5):
                logger.info('Press A to add to hand in 1 second')
                # await self.wait(0.5)
                await self.wait(0.1)
                await self.button_push('a')
            
            # exit while loop
            # break

            # # Sort and exit simultaneously
            await self.button_press('y', 'b')
            await self.wait(0.1)
            await self.button_release('y', 'b')

            # Collect the items
            await self.wait(0.1)
            for _ in range(5):
                await self.button_push('a')
                await self.wait(0.1)

            # Open menu
            await self.button_push('plus')
            await self.wait(0.5) 