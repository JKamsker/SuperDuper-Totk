# to run: joycontrol-pluginloader -r auto SuperDuper-Totk/WallZonai.py

import logging
import asyncio

from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)

class WallZonai(JoycontrolPlugin):
    async def run(self):
        logger.info('Auto Dupe WallZonai Plugin')

        # Press the A button when the controller is ready for input.
        for i in range(3):
            logger.info('Press a for the {} time (of 3)'.format(i+1))
            await self.wait(0.5)
            await self.button_push('a')
            await self.wait(0.5)
        
        logger.info('Pairing completed.')
        

        await self.button_push('plus')
        # Menu variant: use that instead of plus
        # await self.button_push('b')

        await self.wait(0.1)
        while True:
            # Add to hand (Repeat 11 times (1 for activating, 10 for adding))
            for _ in range(11):
                logger.info('Press A to add to hand')
                # await self.wait(0.07)
                # await self.button_push('a', press_time_sec=0.07)
                await self.button_press('a')
                await self.wait(0.075)
                await self.button_release('a')
                await self.wait(0.075)

            await self.wait(0.1)
            
            # # Sort and exit simultaneously
            await self.button_press('y', 'b')
            await self.wait(0.07)
            await self.button_release('y', 'b')

            # Collect the items
            # await self.wait(0.1)
            # for _ in range(5):
            #     await self.button_push('a')
            #     await self.wait(0.1)

            # Open menu
            await self.button_push('plus')
            await self.wait(0.07) 